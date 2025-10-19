```json
{
  "id": "06e2eff550896512",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293220,
  "host_pid": "9e6742732c60:1",
  "hash": "966133e3ab430c26d48e45cbd1fd69f092b61c053dde1d2746f85d24d2a27146",
  "cid": "QmV1966133e3ab430c26d48e45cbd1fd69f092b61c05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293220,
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
      "evaluated_at": 1760293220
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
  "sig": "1abacf25260bef68ad56820b6e8cce8263d705df17b1289f4bb12b93baaec143"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461386979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 72685314, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '1569de4be841c048'}}}