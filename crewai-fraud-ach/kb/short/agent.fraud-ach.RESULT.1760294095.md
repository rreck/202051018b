```json
{
  "id": "e5a47151b95f6830",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294095,
  "host_pid": "9e6742732c60:1",
  "hash": "33c4af3d4e79c81b4ba71f00b625538dd91ad1f743b631b9054bf11efcaaf820",
  "cid": "QmV133c4af3d4e79c81b4ba71f00b625538dd91ad1f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294095,
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
      "evaluated_at": 1760294095
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
  "sig": "dd1a3b8a9ae06127f9772b0d7ea92e3c76b7a8739ee82b12edc1e1abe5e2b113"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 12672429, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}