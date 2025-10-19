```json
{
  "id": "a9b5ed6848bf0c72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290317,
  "host_pid": "9e6742732c60:1",
  "hash": "f500e1ffebd33f35425900ceab63727c790f9a1baa0bcd94635009b0d60231ad",
  "cid": "QmV1f500e1ffebd33f35425900ceab63727c790f9a1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290317,
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
      "evaluated_at": 1760290317
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
  "sig": "0e13e13988c4752cfbf9a2b8ae6f4e3284aa7730063ae95d16d65a6c9b697a35"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464946217
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 75896489, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760284979, 'matching_hash': '76eefa6b67e55304'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}