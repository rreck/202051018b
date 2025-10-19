```json
{
  "id": "5f7cce4f904a0699",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290430,
  "host_pid": "9e6742732c60:1",
  "hash": "816def22a9138e12fd05a6a1e043634bb59e64537de702b0cc08d9a647d584f2",
  "cid": "QmV1816def22a9138e12fd05a6a1e043634bb59e6453",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290430,
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
      "evaluated_at": 1760290430
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
  "sig": "9eca10b58cf9e6926ed39f9cae8ee0507ad9d691952c18d2e93d6a9e112cd68e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599719457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 27878250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '97e4873137c26cd1'}}}