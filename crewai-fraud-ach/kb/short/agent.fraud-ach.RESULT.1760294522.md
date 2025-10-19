```json
{
  "id": "fa492db8f9f734e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294522,
  "host_pid": "9e6742732c60:1",
  "hash": "821243a0424b72b9968c29de0e035cb42851a8f2f33a79298d2046b794be9ae7",
  "cid": "QmV1821243a0424b72b9968c29de0e035cb42851a8f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294522,
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
      "evaluated_at": 1760294522
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
  "sig": "5fb120f5d76d7ce2590b0e42fe37d5542b3e329e6f36b74b5cb6024eefe08cad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 76061272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}