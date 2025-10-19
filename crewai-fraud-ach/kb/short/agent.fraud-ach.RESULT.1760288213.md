```json
{
  "id": "598cc712b83858f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288213,
  "host_pid": "9e6742732c60:1",
  "hash": "a066ece4577c2d08dde1e286062e99f60c0ba956f78782dd2a7db641d6f60313",
  "cid": "QmV1a066ece4577c2d08dde1e286062e99f60c0ba956",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288213,
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
      "evaluated_at": 1760288213
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
  "sig": "9d050305ca817709f17015ab68fc411f433eb10792bd305f097b805479da62a8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021005824
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '58a86144ce85b895'}}}