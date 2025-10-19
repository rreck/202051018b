```json
{
  "id": "e7e5b9f2e70cc2aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293757,
  "host_pid": "9e6742732c60:1",
  "hash": "4403c1a820326a45d2994e5e0a97455e94abab7f58519d04d314b22cfb38b9f4",
  "cid": "QmV14403c1a820326a45d2994e5e0a97455e94abab7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293757,
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
      "evaluated_at": 1760293757
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
  "sig": "7c438344e4b594f11ffedb72d5f5a421909c3c030265cb48cc036561f3293d2e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029303857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 58800150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '4510d576292a5401'}}}