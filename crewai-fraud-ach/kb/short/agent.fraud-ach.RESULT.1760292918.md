```json
{
  "id": "09b0276bdd9b10a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292918,
  "host_pid": "9e6742732c60:1",
  "hash": "8f9a77158a9ee597d509f37b90d65968f910e4061f9a2befecc851dd2e8952b8",
  "cid": "QmV18f9a77158a9ee597d509f37b90d65968f910e406",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292918,
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
      "evaluated_at": 1760292918
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
  "sig": "9745b30f71dec919c4c8e4ba8b9623ec75905f668e43e052e468334996195b19"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 101251488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}