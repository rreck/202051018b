```json
{
  "id": "2c5106a23e409b64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288124,
  "host_pid": "9e6742732c60:1",
  "hash": "a92680a4841a3d2886b5b5528daf86df36d01747dc2efda81c2e0255a16f5bf3",
  "cid": "QmV1a92680a4841a3d2886b5b5528daf86df36d01747",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288124,
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
      "evaluated_at": 1760288124
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
  "sig": "9fd61055c24806cf2943b437f8084044632e549a4bd81d49585ddfce9b874602"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}