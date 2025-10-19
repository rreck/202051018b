```json
{
  "id": "6c06cc915c997e43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294600,
  "host_pid": "9e6742732c60:1",
  "hash": "057eacac4ffa3458eb803f661c178795b94dc4f59f67dc251de6e35b668eca76",
  "cid": "QmV1057eacac4ffa3458eb803f661c178795b94dc4f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294600,
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
      "evaluated_at": 1760294600
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
  "sig": "7b5a4381017845352c3758fcabd90018f4c9de881fbf751cc31c18b9b070587a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274968720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 89925294, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '69fe72c937d65071'}}}