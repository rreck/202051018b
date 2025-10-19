```json
{
  "id": "1bf24af5cee071a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294621,
  "host_pid": "9e6742732c60:1",
  "hash": "37081a54db189d34a03ea07380b5c18ad233884e47a830480331c86eb7f906c7",
  "cid": "QmV137081a54db189d34a03ea07380b5c18ad233884e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294621,
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
      "evaluated_at": 1760294621
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
  "sig": "98164d30f8d3d64f66a2c319b661aec821f3628876164a8c9afd0deb09ee9fa2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025723119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 113650539, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': '7f709c8256c8a242'}}}