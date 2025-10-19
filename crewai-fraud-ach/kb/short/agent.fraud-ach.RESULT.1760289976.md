```json
{
  "id": "986a6482b861ceb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289976,
  "host_pid": "9e6742732c60:1",
  "hash": "eb876c3c38a24654333128e615a8e339b058a019a69a533e61e56fcec6f971ac",
  "cid": "QmV1eb876c3c38a24654333128e615a8e339b058a019",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289976,
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
      "evaluated_at": 1760289977
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
  "sig": "0cf8e963b72246e7bbb6ba8daafe89f73d097fcba49da59de7e8e61b0e711d78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}