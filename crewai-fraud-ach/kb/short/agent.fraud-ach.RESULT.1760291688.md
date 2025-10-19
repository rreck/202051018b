```json
{
  "id": "10a22ce799a7642b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291688,
  "host_pid": "9e6742732c60:1",
  "hash": "2e82b8b6b49a1d00daccab9fb1431d3def438e9921077225d568324bb0d53155",
  "cid": "QmV12e82b8b6b49a1d00daccab9fb1431d3def438e99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291688,
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
      "evaluated_at": 1760291688
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
  "sig": "788c117cf9618847479e956ca49271679d08ea262bf340bae8c71e5733acf551"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591034480
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 73644013, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '8ba7f443842400ac'}}}