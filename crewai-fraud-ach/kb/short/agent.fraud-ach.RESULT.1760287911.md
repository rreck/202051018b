```json
{
  "id": "3f331344bddd6981",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287911,
  "host_pid": "9e6742732c60:1",
  "hash": "7ab41311b7c4dd07facf7dcbe830f8a28c34c74ff7c380a1be34b94752bfa8d8",
  "cid": "QmV17ab41311b7c4dd07facf7dcbe830f8a28c34c74f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287911,
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
      "evaluated_at": 1760287911
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
  "sig": "bbbac45a193093a8c4faf176fffaef0bd6ebf672acfb141fcdf07c2adf4f3db9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597800882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 15610932, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285765, 'matching_hash': 'e972b74e8fc22124'}}}