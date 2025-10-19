```json
{
  "id": "bde96dc7e224ba11",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289403,
  "host_pid": "9e6742732c60:1",
  "hash": "a85f720552566591d9821fec2e90e3ac2b68196b6d4ae88a99311d2f0a6c56ab",
  "cid": "QmV1a85f720552566591d9821fec2e90e3ac2b68196b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289403,
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
      "evaluated_at": 1760289403
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
  "sig": "77cdf26833f65b06e96093ea6fa4b8a1322556f64c0dd583f5c9bbd3b42742f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027064013
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 36311348, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': '811cb7a859f68158'}}}