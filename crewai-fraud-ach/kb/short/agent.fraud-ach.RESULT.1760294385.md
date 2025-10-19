```json
{
  "id": "824d0c75cfa85eb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294385,
  "host_pid": "9e6742732c60:1",
  "hash": "e2a3ca43a10918fd0ff013e6f23a7871f9408e2b312fb782c7a68b366ad65ee6",
  "cid": "QmV1e2a3ca43a10918fd0ff013e6f23a7871f9408e2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294385,
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
      "evaluated_at": 1760294385
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
  "sig": "3ad666784aab20c11724c386fe2a38bf9e9ac661fe842cb2fde382e7ca39ad4c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278619879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 80273559, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'bfc334a18daf8fbf'}}}