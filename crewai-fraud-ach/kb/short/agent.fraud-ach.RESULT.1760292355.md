```json
{
  "id": "217ce0c8309617ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292355,
  "host_pid": "9e6742732c60:1",
  "hash": "2fc51c7e03b0fa7e0839fbe490c75f3d3d710c08a76379d0df70c5c04342e59d",
  "cid": "QmV12fc51c7e03b0fa7e0839fbe490c75f3d3d710c08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292355,
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
      "evaluated_at": 1760292355
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
  "sig": "506be888995f22b8561ed7069c597cd576e608c376ad6788d11e1587da8a6e8b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026803563
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 49168952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}