```json
{
  "id": "0256380004ff1d12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294332,
  "host_pid": "9e6742732c60:1",
  "hash": "8f13170deb75d7a2f3030cc8e06cfc8023c468ccb147402916e7ac24eb5d14f1",
  "cid": "QmV18f13170deb75d7a2f3030cc8e06cfc8023c468cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294332,
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
      "evaluated_at": 1760294332
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
  "sig": "f68d13522c862f03b54e7f79f379477736b94b1364549c2feeadd775ab237580"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465723283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 100899204, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285764, 'matching_hash': 'e1350af409930159'}}}