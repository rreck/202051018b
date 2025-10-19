```json
{
  "id": "1ec67cc9e8b97ebd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293538,
  "host_pid": "9e6742732c60:1",
  "hash": "7764afe74231dada1bceffa77202dcfd9215aee89409d1b65181cc19c298f7af",
  "cid": "QmV17764afe74231dada1bceffa77202dcfd9215aee8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293538,
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
      "evaluated_at": 1760293538
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
  "sig": "0d31281a429d85c113e116203c520ca13ddbb7fe48984f36b0291eee8d51cdeb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276932154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 80984200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': '117d4b1b88487dad'}}}