```json
{
  "id": "0c13a7df84300700",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291001,
  "host_pid": "9e6742732c60:1",
  "hash": "fb78f623a102c69f37b39d15915c1b2919daed04091397d2f87f261842a100af",
  "cid": "QmV1fb78f623a102c69f37b39d15915c1b2919daed04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291001,
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
      "evaluated_at": 1760291001
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
  "sig": "a3044177f81192360d8ab4b755163b81a92f0af9c0b27d985832aa2ba8d1d07c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 52192672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}