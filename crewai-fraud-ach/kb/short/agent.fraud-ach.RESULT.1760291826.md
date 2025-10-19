```json
{
  "id": "01b407b4d18effb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291826,
  "host_pid": "9e6742732c60:1",
  "hash": "3a2667cba1215578d3b6c6082aa6b175fba939eb757535e93b7de457edb20faf",
  "cid": "QmV13a2667cba1215578d3b6c6082aa6b175fba939eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291826,
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
      "evaluated_at": 1760291826
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
  "sig": "a69f11c03db4f1cd256cc64b746986e8f5beef64f7bf9f4c0789a2a94ed0b2a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024174154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 78331560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '443a0c3eda74d322'}}}