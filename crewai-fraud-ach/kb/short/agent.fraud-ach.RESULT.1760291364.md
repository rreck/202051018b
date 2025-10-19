```json
{
  "id": "747bb7d18d45bf8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291364,
  "host_pid": "9e6742732c60:1",
  "hash": "3e11c31b426f4b403754d8821442ead2c9ae29381c4a8d7c3ad315e432123d1a",
  "cid": "QmV13e11c31b426f4b403754d8821442ead2c9ae2938",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291364,
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
      "evaluated_at": 1760291364
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
  "sig": "4972bda5836e3e92de62e43adf4cdf46c8ee7e3a5cf1f5f199226180530d2af8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152729668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 24262558, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': 'e33e77be4df2721a'}}}