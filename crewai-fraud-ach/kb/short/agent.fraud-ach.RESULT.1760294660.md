```json
{
  "id": "e5e50b9a4881d38f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294660,
  "host_pid": "9e6742732c60:1",
  "hash": "40d60a5c3580838e6246d8f768cf813115f95ab11b931681bc3e02d22996592b",
  "cid": "QmV140d60a5c3580838e6246d8f768cf813115f95ab1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294660,
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
      "evaluated_at": 1760294660
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
  "sig": "de72d2e5bd157828aa81e96e2e114601976410085cce394424d461d7355d9ea6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468543646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 114457530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '526960b6a0cd6e16'}}}