```json
{
  "id": "4ee56a6d35bffc0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293471,
  "host_pid": "9e6742732c60:1",
  "hash": "a8b117a596b063c98f2872e796fde91213bedd76dd73d046eb4441cd9549da0a",
  "cid": "QmV1a8b117a596b063c98f2872e796fde91213bedd76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293471,
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
      "evaluated_at": 1760293471
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
  "sig": "0a2b603e0fac6ef39aa503b99c453b227ab284b3f188a4bacbf611a10076ee3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274458495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 99909771, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': '191d9163e8e6657e'}}}