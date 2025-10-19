```json
{
  "id": "3e14841802a0c00a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287549,
  "host_pid": "9e6742732c60:1",
  "hash": "898d3671ca33a38b210a5f5c05933281a6986b999144a19c72aac22ca477672e",
  "cid": "QmV1898d3671ca33a38b210a5f5c05933281a6986b99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287549,
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
      "evaluated_at": 1760287549
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
  "sig": "998c3ee262e6fdc79a85c1b76392859f6de846de22daa07150637b8d1964dfff"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 121000245569369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 15447232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285764, 'matching_hash': '9f2120bc546d4049'}}}