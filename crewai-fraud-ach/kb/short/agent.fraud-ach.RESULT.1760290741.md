```json
{
  "id": "65608108d8e03380",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290741,
  "host_pid": "9e6742732c60:1",
  "hash": "089cc154dbb9d448399fafdca9482d280cef0888c780986bcc7abca5787fa4bf",
  "cid": "QmV1089cc154dbb9d448399fafdca9482d280cef0888",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290741,
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
      "evaluated_at": 1760290741
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
  "sig": "10c5392774b2d37e9b81d3e2b10e6d860e49f35b596ec8493a6fbe368b502e4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242854691
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 29210250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': '6f29fe2a1ce5e88d'}}}