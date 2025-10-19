```json
{
  "id": "3d8811beaf920970",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289672,
  "host_pid": "9e6742732c60:1",
  "hash": "c1aec09b3d632cf05e4feb19dde056ea815327114ed95f3ce5db10e1db0673a9",
  "cid": "QmV1c1aec09b3d632cf05e4feb19dde056ea81532711",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289672,
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
      "evaluated_at": 1760289672
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
  "sig": "931922f0eaf67b109c50659120082c04d33bc8d0c5cde00a88cfa0c44df6fafe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242021792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 56043520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': '6b62929422267286'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}