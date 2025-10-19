```json
{
  "id": "a8139320e9b632aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288284,
  "host_pid": "9e6742732c60:1",
  "hash": "d27a578dfd8c0f86a28cd81c4f62c761e795a493395243057ed9f31eb0db4281",
  "cid": "QmV1d27a578dfd8c0f86a28cd81c4f62c761e795a493",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288284,
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
      "evaluated_at": 1760288284
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
  "sig": "61b3e238b64b3786b7bf40af50fd7aed0e0b6b174b0ab9523052832f62f2ccee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 28005824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}