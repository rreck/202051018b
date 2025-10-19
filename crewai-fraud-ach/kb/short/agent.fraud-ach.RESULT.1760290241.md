```json
{
  "id": "ba1605831aec1370",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290241,
  "host_pid": "9e6742732c60:1",
  "hash": "40112d2a1e39d1967bf0432fcea97e24d44af292eb4a451e0979c7b27bf31aba",
  "cid": "QmV140112d2a1e39d1967bf0432fcea97e24d44af292",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290241,
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
      "evaluated_at": 1760290241
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
  "sig": "1987c85168eac82e1c2427f411283fd7e9a27242d1cc25fd14de7c7ea95c587c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023759733
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 33415830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': 'cdd972b8484ef71b'}}}