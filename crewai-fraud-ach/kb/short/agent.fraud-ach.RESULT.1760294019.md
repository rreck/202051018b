```json
{
  "id": "09cfd7c3590208f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294019,
  "host_pid": "9e6742732c60:1",
  "hash": "6715b292cf1404c425371a1d414e0dc6b94f5fd95b9932a9792343d2009292fb",
  "cid": "QmV16715b292cf1404c425371a1d414e0dc6b94f5fd9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294019,
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
      "evaluated_at": 1760294019
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
  "sig": "b9f9623521e506eba1219d31c33658bb4ebbd50046c2d0de4e4867b762a15561"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024349722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 14956210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '3e275568f5204778'}}}}