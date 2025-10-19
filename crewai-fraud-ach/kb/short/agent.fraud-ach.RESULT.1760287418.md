```json
{
  "id": "2ce650d002663802",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287418,
  "host_pid": "9e6742732c60:1",
  "hash": "581d4acfc01abf12d22df79dc5521199982115118f03c84d01f1094f3dda11a4",
  "cid": "QmV1581d4acfc01abf12d22df79dc552119998211511",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287418,
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
      "evaluated_at": 1760287418
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "ed859e1fa2055f9ca9d61d898ed3b611e20e156b573cb04b331060443a15c6eb"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 28081463, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}