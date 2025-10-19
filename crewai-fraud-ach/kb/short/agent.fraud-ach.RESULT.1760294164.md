```json
{
  "id": "8deb458304a8f0a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294164,
  "host_pid": "9e6742732c60:1",
  "hash": "79341deeef603102fc168c4fec0c7ffffabb50bc1b03cf6dfd2a3c02b763ba33",
  "cid": "QmV179341deeef603102fc168c4fec0c7ffffabb50bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294164,
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
      "evaluated_at": 1760294164
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
  "sig": "2bfc41f8330fb483ea6a4ffac74525ea264479717a3ba39607ac77d49aa6b4c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249862639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 80143845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '8cd9f1a7b8ce269f'}}}