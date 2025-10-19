```json
{
  "id": "611dd5a3fc8413f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289602,
  "host_pid": "9e6742732c60:1",
  "hash": "3264922e7aa658b24bcc307747ee35759b224319026ec23626c700f98ca52f1a",
  "cid": "QmV13264922e7aa658b24bcc307747ee35759b224319",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289602,
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
      "evaluated_at": 1760289602
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
  "sig": "3566769b103123694a2b1b1661971b76ffccdf645932f32b48e76de2e79d288c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151297418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 55855744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '6f92d94cce52eccd'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '361190711', 'validation_error': 'Invalid routing number checksum'}}}