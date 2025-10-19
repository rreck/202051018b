```json
{
  "id": "e62613deb3db8e84",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286552,
  "host_pid": "9e6742732c60:1",
  "hash": "11d987341e393179e1f6cb60034f46742405635e63ba81652cf0a548b7395e10",
  "cid": "QmV111d987341e393179e1f6cb60034f46742405635e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286552,
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
      "evaluated_at": 1760286552
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
  "sig": "9c8333ce4906b03888d90f7abbcc70a9174243a3080d907ba8b4a2bf5fbe6c2a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009595535562
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': '052e7693e8a3f40d'}}}, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285764, 'matching_hash': '39c5bac7d3007e29'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}