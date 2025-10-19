```json
{
  "id": "f59519aa9b946d8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287791,
  "host_pid": "9e6742732c60:1",
  "hash": "c925391df9103b4a3f18b6ecbe03c6c84e69fcbf4f0a3407363f952dc5935278",
  "cid": "QmV1c925391df9103b4a3f18b6ecbe03c6c84e69fcbf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287791,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760287791
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "af7066d8c67e158c08e843ad84166e636933ef4c749a3e5ebc9609b16d56119b"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 026009593711033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 19916424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}