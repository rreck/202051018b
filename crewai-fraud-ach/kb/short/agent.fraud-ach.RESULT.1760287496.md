```json
{
  "id": "936c15f0c1a9fb4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287496,
  "host_pid": "9e6742732c60:1",
  "hash": "c5e6a72c0793a1a77dfcceba17e7030af26a28e93323f92239289ded9ae10f5a",
  "cid": "QmV1c5e6a72c0793a1a77dfcceba17e7030af26a28e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287496,
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
      "evaluated_at": 1760287496
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8f7b94236dbbc0d2a56cd22045d9c4977ca8ba3feaf18b06dbfe9208d24e2bf3"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 111000025121499
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': 'a696ea0f650f1de2'}}}