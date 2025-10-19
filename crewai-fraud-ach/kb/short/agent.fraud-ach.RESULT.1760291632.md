```json
{
  "id": "b9cfe854d7022dc1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291632,
  "host_pid": "9e6742732c60:1",
  "hash": "e412a8d4b18f0f59be245ef5b0f223f25e1390c67eea6f624f3a2fc85d9d6e0a",
  "cid": "QmV1e412a8d4b18f0f59be245ef5b0f223f25e1390c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291632,
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
      "evaluated_at": 1760291632
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
  "sig": "92d51fde19521941d6f96abc4cfc323280bdab36edb2c821d1a173db1c4f4611"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 85196303, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}