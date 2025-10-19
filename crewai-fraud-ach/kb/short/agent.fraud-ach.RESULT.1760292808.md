```json
{
  "id": "1e60919347c2436f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292808,
  "host_pid": "9e6742732c60:1",
  "hash": "610084eddc271962dfb7309df8df8f9561b018bced4f890abc730ebcb9e0ab66",
  "cid": "QmV1610084eddc271962dfb7309df8df8f9561b018bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292808,
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
      "evaluated_at": 1760292808
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
  "sig": "007fde58790e7d2a65ac3904cb115d16651a42d9f691d373460373f2d09ff801"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 11246095, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}