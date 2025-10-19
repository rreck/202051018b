```json
{
  "id": "87f19d2b56c20c24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294710,
  "host_pid": "9e6742732c60:1",
  "hash": "1c6af831f2392d51bfdcb141f62cae212bad2e9b0e0ea356fb703bb2f610bb70",
  "cid": "QmV11c6af831f2392d51bfdcb141f62cae212bad2e9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294710,
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
      "evaluated_at": 1760294710
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
  "sig": "2c6687c1f453afc7a567a6c4b971675a884e86dceb86384d69a7d168589e9cf2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595764750
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 23039559, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '81dd493231a1d242'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}