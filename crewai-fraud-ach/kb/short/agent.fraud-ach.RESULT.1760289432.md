```json
{
  "id": "e9c78bbae11c1573",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289432,
  "host_pid": "9e6742732c60:1",
  "hash": "5e880840568387df35b38c8d47d0ef67ebb0584026d93a22ff3e9dd02c81925c",
  "cid": "QmV15e880840568387df35b38c8d47d0ef67ebb05840",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289432,
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
      "evaluated_at": 1760289432
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
  "sig": "996c56d4d18ec13516e68c06a7c112a58962f46d9546705a3bfe9218a01ec238"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271137444
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 27872538, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': 'cc450f1d426424de'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}