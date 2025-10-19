```json
{
  "id": "0aed7eca4bb45888",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294444,
  "host_pid": "9e6742732c60:1",
  "hash": "6adfe91f96d00f49bed71052b889b24fbae2cc2e25d25a5440259ce3aa406cac",
  "cid": "QmV16adfe91f96d00f49bed71052b889b24fbae2cc2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294444,
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
      "evaluated_at": 1760294444
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
  "sig": "719b5ef67103de62672732173a18e1e7c10da0822c26a10972c18f8c565b3e3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595526763
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 82881358, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': '4e9c09a811d09ae3'}}}