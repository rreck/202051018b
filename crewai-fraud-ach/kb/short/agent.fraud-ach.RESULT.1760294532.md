```json
{
  "id": "0649534be7e0082c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294532,
  "host_pid": "9e6742732c60:1",
  "hash": "32f8e68331c593abbb9c1a68d84dfe10379ca486316dd398ff8131629dfbda4b",
  "cid": "QmV132f8e68331c593abbb9c1a68d84dfe10379ca486",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294532,
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
      "evaluated_at": 1760294532
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
  "sig": "c6e7395171460d31c7cd85c30df27b34b3f6234a2a8f3d539f7361ac1d4dd627"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155806195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 56681520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '37264973f9c39fe3'}}}