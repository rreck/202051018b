```json
{
  "id": "a883bddac23ac7aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288120,
  "host_pid": "9e6742732c60:1",
  "hash": "57d3268816aef36623cbfda04ef2e7143548cb3df5561ebf7b37f56dd3e1f9dd",
  "cid": "QmV157d3268816aef36623cbfda04ef2e7143548cb3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288120,
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
      "evaluated_at": 1760288120
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
  "sig": "04bcbe8afdb9c3452b4026786f2cb42b46c8f1f7420fd0ed38b2647c5f73d934"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021660412
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 26740193, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285764, 'matching_hash': '19be1dcf8b4c513c'}}}