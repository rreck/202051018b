```json
{
  "id": "a90ba6c67501ba91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294180,
  "host_pid": "9e6742732c60:1",
  "hash": "a20bffdfc1526cab361a6a882c5496a4165df44613cd893fe9d1871a4f3dc972",
  "cid": "QmV1a20bffdfc1526cab361a6a882c5496a4165df446",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294180,
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
      "evaluated_at": 1760294180
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
  "sig": "7454e7184a3f4a069f6117e374120f14158eeb9061a7c83338d805be51765334"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598880520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 44378112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': '9fe1b03994749115'}}}