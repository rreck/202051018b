```json
{
  "id": "3e572e2354e6d5fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294603,
  "host_pid": "9e6742732c60:1",
  "hash": "39087c87ef1ee5628a419ce371d06a8762187275d1a11952e86baa79a8fcef36",
  "cid": "QmV139087c87ef1ee5628a419ce371d06a8762187275",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294603,
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
      "evaluated_at": 1760294603
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
  "sig": "f39d00b436742da3dc24028e6db8a24a49c4c49cb0d54f08fc25a3db86d46f53"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028559782
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 53838918, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '551fe21bbee5d648'}}}