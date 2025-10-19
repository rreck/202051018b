```json
{
  "id": "50d3e773136c532f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290994,
  "host_pid": "9e6742732c60:1",
  "hash": "00a8c40f387bd14574cdba9681134041ad4f2dc68c0615654bc9b7e42c7e76c1",
  "cid": "QmV100a8c40f387bd14574cdba9681134041ad4f2dc6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290994,
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
      "evaluated_at": 1760290994
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
  "sig": "e75158b2d4b93e0cc408f736e734042bbc3e74b14cb82977b5130994ad0537ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 70843244, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285764, 'matching_hash': '100dee2bbeee5c05'}}}