```json
{
  "id": "277299131678504d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287673,
  "host_pid": "9e6742732c60:1",
  "hash": "e4f31a2260bd8641bf39c24720a220d2b1a7914e8967b247c2b0cc68a38bdcbf",
  "cid": "QmV1e4f31a2260bd8641bf39c24720a220d2b1a7914e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287673,
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
      "evaluated_at": 1760287673
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
  "sig": "31ce040beea33d79e35d7cec8f18a2e7e84625be604bebe14c147deea58d39db"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 22741104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}