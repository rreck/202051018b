```json
{
  "id": "42b9b1d26ec55f01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288219,
  "host_pid": "9e6742732c60:1",
  "hash": "9baf456032b57c160ac32eb033884da97a5b1d54df1d3d3ace613f99f1e4ee4e",
  "cid": "QmV19baf456032b57c160ac32eb033884da97a5b1d54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288219,
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
      "evaluated_at": 1760288219
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "3b91b4980790e8919834665322bdf758cc47fd027ac2d8790cbb20b1b1508c11"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 026009597287610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 86000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285765, 'matching_hash': 'd127b5f232f25796'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}