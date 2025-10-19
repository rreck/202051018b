```json
{
  "id": "c1b2a17cba97349d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290432,
  "host_pid": "9e6742732c60:1",
  "hash": "c9ada027c96670e3bf9f493fda81de2e1157fdfab7d54282dbb50f8d3f512be9",
  "cid": "QmV1c9ada027c96670e3bf9f493fda81de2e1157fdfa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290432,
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
      "evaluated_at": 1760290432
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
  "sig": "2194c7709e483cc9be4b5bc6c8114bcc8a3f153aad5e294939002b242634db89"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468454923
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 16554900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}