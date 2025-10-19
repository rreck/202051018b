```json
{
  "id": "bee9057117b238a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291671,
  "host_pid": "9e6742732c60:1",
  "hash": "3501a4cef862af64ad18699e0ca1fb58b9a7b7e289c8d8f5088625cf49fc81ca",
  "cid": "QmV13501a4cef862af64ad18699e0ca1fb58b9a7b7e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291671,
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
      "evaluated_at": 1760291671
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
  "sig": "ed6db9560a23ba460ffda2aed91f2900b43994e28133b6faa976202fa5c3d2c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 15171660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}