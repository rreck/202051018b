```json
{
  "id": "12d7db1b29a7e3fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294865,
  "host_pid": "9e6742732c60:1",
  "hash": "78504ae7334ef90bc5702273127ab3eaf902b572bf15ce455c57194a231c902e",
  "cid": "QmV178504ae7334ef90bc5702273127ab3eaf902b572",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294865,
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
      "evaluated_at": 1760294865
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
  "sig": "5ae1704d36de068aa24dd2ae1f98b939e08d41347858e68b7d722ef5b258f4ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469776996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 40417800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}