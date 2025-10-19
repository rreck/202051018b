```json
{
  "id": "4a606500549f27fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291914,
  "host_pid": "9e6742732c60:1",
  "hash": "16ee9390889d42cb26f84aadb0e56eedef05eed5e695f20d55fa82fafb2b4a27",
  "cid": "QmV116ee9390889d42cb26f84aadb0e56eedef05eed5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291914,
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
      "evaluated_at": 1760291914
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
  "sig": "314372d2a81a66f3423a01a8db76351f1fa1dd12f5869bebd0ea82bc45ee8979"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243661505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 77741676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285764, 'matching_hash': '37851bbce8ea73db'}}}