```json
{
  "id": "f6882e77046bbf36",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290703,
  "host_pid": "9e6742732c60:1",
  "hash": "f781c846ba40101e424885172b111a6535b263ff99a61918fac0df788059c26b",
  "cid": "QmV1f781c846ba40101e424885172b111a6535b263ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290703,
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
      "evaluated_at": 1760290703
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
  "sig": "4603cb0fbbcfcc65ffd9b2647f3b9ac050bfab768bf95131072b4d7ebe6963f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595535562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 21225929, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '052e7693e8a3f40d'}}}