```json
{
  "id": "5eb554e64580b0b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294769,
  "host_pid": "9e6742732c60:1",
  "hash": "84d2761c31c4836c5b81b609f9ef616a606783b0c308614a283b7cb41ed93396",
  "cid": "QmV184d2761c31c4836c5b81b609f9ef616a606783b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294769,
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
      "evaluated_at": 1760294769
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
  "sig": "f53c1d7f8110816b1aa56305e81cacab44e6d4335697f41ac8dc3ea51128c952"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242680908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 84120952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': '8e78dc9e18bacaa7'}}}